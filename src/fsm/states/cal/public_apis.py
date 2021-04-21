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
from fsm.states.cal.impl import *

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
    status = rental_fsm_machine.error_types.SM_NO_ERROR
    eventVal = currEvent.rental_fsm_event
    # print("rental_fsm_cal_process()")

    cObj = sharedMemory_Cal()
    c = cObj.getCalObj()
    errorStatus = c.calculate()
    if(errorStatus == False):
        currEvent.event = event.rental_fsm_event.SUCCEEDED
        next_state = rental_fsm_machine.rental_fsm_states.RENTAL_FSM_PRINT;
    else:
        currEvent.event = event.rental_fsm_event.FAILED
        next_state = rental_fsm_machine.rental_fsm_states.RENTAL_FSM_INPUT;

    # m = sharedM.getFSMObject()
    # printState(m.currState)
    # printState(machine.currState)
    # printEvent(currEvent)
    return(status, next_state, eventVal)
