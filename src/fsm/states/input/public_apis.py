'''
 * @file        public_apis.py
 * @ingroup     input
 * @brief       Files containing public-facing APIs
 *
 * Contains definitions of public  APIs specific to the input state
 *
'''

from fsm.types.fsm_types import *
from fsm.helpers.print_apis import *
from fsm.states.input.mechanics import *

'''
 * @brief State process function
 *
 * This function is the process function for current state. 
 *
 * @param machine - state machine identifier
 * @param currEvent   - event class (includes the event and also its type)
 *
 * @return standardized status code
'''
def rental_fsm_input_process(machine, currEvent):
    (status, next_state, eventVal) = process_input_state(machine, currEvent)
    return(status, next_state, eventVal)

