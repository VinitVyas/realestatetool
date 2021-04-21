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
from fsm.states.input.impl import *


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
    status = rental_fsm_machine.error_types.SM_NO_ERROR
    next_state = rental_fsm_machine.rental_fsm_states.RENTAL_FSM_CAL;

    # print("rental_fsm_input_process()")
    # printEvent(currEvent)
    # m = sharedM.getFSMObject()
    # printState(m.currState)
    # printState(machine.currState)

    ipObj = sharedMemory_Input()
    ip = ipObj.getInputObj()
    errorStatus = ip.getInputFromUser()
    # print("rental_fsm_input_process(): ipObj{}".format(ipObj))
    # print("rental_fsm_input_process(): ip{}".format(ip))
    if(errorStatus == False):
        currEvent.event = event.rental_fsm_event.SUCCEEDED
    else:
        currEvent.event = event.rental_fsm_event.FAILED

    return(status, next_state, currEvent.rental_fsm_event)

