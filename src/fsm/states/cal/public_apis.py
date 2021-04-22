'''
 * @file        public_apis.py
 * @ingroup     cal
 * @brief       Files containing public APIs
 *
 * Contains definitions of public APIs specific to the current state
 *
'''
from fsm.types.fsm_types import *
from fsm.helpers.print_apis import *
from fsm.states.cal.mechanics import *

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
def rental_fsm_cal_process(machine, currEvent):
    (status, next_state, eventVal) = process_cal_state(machine, currEvent)
    return (status, next_state, eventVal)