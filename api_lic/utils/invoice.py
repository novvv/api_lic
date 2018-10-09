from reportlab.lib.pagesizes import letter,A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.platypus.flowables import KeepTogether
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, \
    Frame, BaseDocTemplate, PageTemplate, FrameBreak,TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER,TA_RIGHT,TA_JUSTIFY

from api_lic import model,settings


class InvoiceRender(object):
    def __init__(self, data, filename):
        self._data = data
        self._filename = filename
        self._logo = data.logo
        self._doc = None
        self._story = []
        self._frame = None

        style_sheet = getSampleStyleSheet()
        self._style = style_sheet["BodyText"]
        self._t_style = ParagraphStyle(
            name='Tables', leftIndent=40, rightIndent=40)
    def generate(self):
        # self._doc = SimpleDocTemplate(
        #     self._filename, pagesize=letter)
        self._doc = BaseDocTemplate(
            self._filename, pagesize=letter)
        page_width, page_height = letter
        self._frame = Frame(
            self._doc.leftMargin, self._doc.bottomMargin,
            self._doc.width, self._doc.height,
            leftPadding=10, rightPadding=10,
            showBoundary=0)
        self._doc.addPageTemplates(
            [PageTemplate(id='Col', onPage=self._add_page_number, frames=[self._frame]), ])

        self._story.append(self._render_header())
        self._story.append(Spacer(page_width, 30))
        if hasattr(self._data,'recurring_charges') and self._data.recurring_charges:######
             self._story.append(self._render_summary())
        if hasattr(self._data,'transaction_summary') and len(self._data.transaction_summary):
             self._story.append(KeepTogether(self._render_transaction_summary_analysis()))
        # if self._data['show_authorization_code_summary']:
        #     self._story.append(KeepTogether(self._render_authorization_code_summary_report()))
        # if self._data['show_all_area_codes_summary']:
        #     self._story.append(KeepTogether(self._render_all_area_codes_summary_report()))
        # if self._data['show_origination_lata_summary']:
        #     self._story.append(KeepTogether(self._render_origination_lata_summary_report()))
        self._story.append(Spacer(page_width, 30))
        self._story.append(self._render_footer())

        self._doc.build(self._story)

        return True

    def _add_page_number(self, canvas, doc):
        page_num = canvas.getPageNumber()
        text = "Page #%s" % page_num
        canvas.drawRightString(200 * mm, 20 * mm, text)
        # self._frame.drawBackground(canvas)

    @staticmethod
    def _get_total_by_column(table, column, column_type=float, round_digits=2):
        return round(
            sum([column_type(row[column]) for row in table]), round_digits)

    def _para(self, content):
        # adding check in case the content is None
        if content == None:
            return Paragraph(" ", self._style)

        return Paragraph(content, self._style)

    def _t_para(self, content):
        # adding check in case the content is None
        if content == None:
            return Paragraph(" ", self._t_style)
        return Paragraph(content, self._t_style)

    def _para_bank_info(self):
        if self._data.pdf_tpl == None:
            return self._para(" ")
        return self._para(self._data.pdf_tpl)

    def _render_footer(self):
        data = [
            ["", "", ""],
            [
                self._para_bank_info() if self._data.tpl_number == 0 else "",
                self._para_bank_info() if self._data.tpl_number == 2 else "",
                ""
            ],
            ["", "", ""],
        ]
        return Table(
            data,
            style=[
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('TOPPADDING', (0, 0), (-1, -1), 0),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ])

    def _render_header(self):
        if self._logo:
            logo = Image(self._logo)
            logo.drawHeight = 0.5 * inch
            logo.drawWidth = 1 * inch
        else:
            logo = ''

        c_name = self._para(
            "<para align=right><font size=9><b>Billed to:</b> {}</font></para>".format(
                self._data.company.company_name))
        inv_number = self._para(
            "<para align=right><font size=9><b>Invoice#:</b> {}</font></para>".format(
                self._data.invoice_number))
        inv_date = self._para(
            "<para align=right><font size=9><b>Invoice Date:</b> {}</font></para>".format(
                self._data.created_on))
        due_date = self._para(
            "<para align=right><font size=9><b>Payment Due Date:</b> {}</font></para>".format(
                self._data.created_on))
        billing_period = self._para(
            "<para align=right><font size=9><b>Billing Period:</b> {}-{}</font></para>".format(
                self._data.invoice_start_date,self._data.invoice_end_date))
        client_data = [
            [c_name],
            [inv_number],
            [inv_date],
            [due_date],
            [billing_period],
        ]
        client_table = Table(
            client_data,
            style=[
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('TOPPADDING', (0, 0), (-1, -1), 0),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ])

        p_name = self._para(self._data.created_by)
        p_bank = self._para_bank_info() if self._data.tpl_number == 1 else ""
        data = [
            [logo, ""],
            ["", ""],
            [p_name, client_table],
            ["", ""],
            [p_bank, ""],
        ]
        return Table(
            data,
            style=[
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('TOPPADDING', (0, 0), (-1, -1), 0),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ])
    
    def _render_summary(self):
        account_summary = self._para(
            "<b><font size=11>Account Summary</font></b>")
        balance_label = self._para("<font size=9>Account Balance</font>")
        balance = self._para(
            "<b><font size=9>{}</font></b>".format(self._data.company.balance))
        recurring_charges_label = self._para(
            "<font size=9>Recurring Charges</font>")
        recurring_charges = self._para(
            "<b><font size=9>{}</font></b>".format(self._data.recurring_charges))
        amount_due_label = self._para("<font size=9>Amount Due</font>")
        amount_due = self._para(
            "<b><font size=9>{}</font></b>".format(self._data.amount))
        due_date_label = self._para("<font size=9>Due Date</font>")
        due_date = self._para(
            "<b><font size=9>{}</font></b>".format(self._data.due_date))
        data = [
            [account_summary, ""],
            [balance_label, balance],
            [recurring_charges_label, recurring_charges],
            [amount_due_label, amount_due],
            [due_date_label, due_date],
        ]
        return Table(
            data,
            style=[
                ('BOTTOMPADDING', (0, 0), (1, 0), 4),
                ('TOPPADDING', (0, 1), (-1, -1), 0),
                ('BOTTOMPADDING', (0, 1), (-1, -1), 0),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('SPAN', (0, 0), (1, 0)),
                ('LINEABOVE', (0, 1), (1, 1), 0.5, colors.black),
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f4f4f4')),
            ])
    
    def _render_transaction_summary_analysis(self):
        table_header = self._para(
            "<b><font size=11>Transaction Summary Analysis</font></b>")
        date_label = self._para("<b><font size=9>Date</font></b>")
        description_label = self._para(
            "<b><font size=9>Description</font></b>")
        amount_label = self._para("<b><font size=9>Amount</font></b>")
        data = [
            [table_header, "", ""],
            ["", "", ""],
            [date_label, description_label, amount_label],
        ]
        inner_data = self._data.transaction_summary
        data.extend(inner_data)
        return Table(
            data,
            style=[
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f4f4f4')),
                ('SPAN', (0, 0), (2, 0)),
                ('LINEABOVE', (0, 1), (2, 1), 0.5, colors.black),
                ('BACKGROUND', (0, 2), (2, 2), colors.HexColor('#b5b5b5')),
                ('BACKGROUND', (0, 3), (-1, -1), colors.HexColor('#e5e5e5')),
                ('INNERGRID', (0, 2), (-1, -1), 0.5, colors.white),
                ('ALIGN', (2, 3), (2, -1), 'RIGHT'),
            ])

if __name__ == "__main__":
    from datetime import datetime,timedelta
    import os
    model.init_db()
    inv = model.Invoice.query().first()
    # inv.pdf_tpl = None
    # inv.tpl_number = 0
    # inv.transaction_summary = [('2018-01-01','charges',12.34)]
    # inv.recurring_charges = 12.34
    # inv.due_date = inv.invoice_end_date+timedelta(days=45)
    doc = InvoiceRender(inv,"example.pdf")
    doc.generate()
    os.system('okular example.pdf')
