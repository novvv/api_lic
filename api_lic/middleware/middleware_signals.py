from falcon_rest.signals import Signal


process_request_start = type('ProcessRequestStart', (Signal, ), dict())()
process_request_end = type('ProcessRequestEnd', (Signal, ), dict())()

process_resource_start = type('ProcessResourceStart', (Signal, ), dict())()
process_resource_end = type('ProcessResourceEnd', (Signal, ), dict())()

process_response_start = type('ProcessResponseStart', (Signal, ), dict())()
process_response_end = type('ProcessResponseEnd', (Signal, ), dict())()

token_incorrect = type('TokenIncorrect', (Signal, ), dict())()
token_expired = type('TokenExpired', (Signal, ), dict())()
