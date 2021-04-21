'''
 *
 * @file        public_apis.py
 * @ingroup     print
 * @brief       Files containing public APIs
 *
 * Contains definitions of public APIs specific to the print state
 *
'''

from fsm.types.fsm_types import *
from fsm.helpers.print_apis import *
from fsm.states.print.impl import *

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
def rental_fsm_print_process(machine, currEvent):
    status = rental_fsm_machine.error_types.SM_NO_ERROR
    eventVal = currEvent.rental_fsm_event
    # print("rental_fsm_print_process()")
    # printEvent(currEvent)

    smp = SharedMemory_Print()
    p = smp.getPrintObj()

    errorStatus = p.printAllData()
    if(errorStatus == False):
        currEvent.event = event.rental_fsm_event.SUCCEEDED
        next_state = rental_fsm_machine.rental_fsm_states.RENTAL_FSM_END;
    else:
        currEvent.event = event.rental_fsm_event.FAILED
        next_state = rental_fsm_machine.rental_fsm_states.RENTAL_FSM_PRINT;

    return(status, next_state, eventVal)
