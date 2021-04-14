'''
 * @file        private_module_cal.py
 * @ingroup     src
 * @brief       Files containing internal/private APIs for the current state
 *
 * Contains definitions of APIs specific to the current state
 *
'''
from fsm_types import *
from fsm_api import *
from private_module_state2_impl import *

'''
 * @brief Validate the next state for current state
 *
 * This function is design to check that the requested state transition can be allowed for the current state.
 *
 * @param event         - event
 * @param next_state    - next state to move to
 *
 * @return standardized status code
'''
def rental_fsm_cal_validate(currEvent, next_state):
    # print("rental_fsm_cal_validate()")
    # print("Debug: EventType: {}".format(currEvent.eventType))
    # print("Debug: Event: {}".format(currEvent.event))

    status = rental_fsm_machine.error_types.SM_INVALID_TRANSITION
   
    if(currEvent.eventType != event.rental_fsm_event_type.RENTAL_FSM_MSG):
        if(currEvent.event == event.rental_fsm_event.SUCCEEDED):
            
            if(next_state == rental_fsm_machine.rental_fsm_states.RENTAL_FSM_PRINT):
                status = rental_fsm_machine.error_types.SM_NO_ERROR
            
        elif(currEvent.event == event.rental_fsm_event.FAILED):
            
            if(next_state == rental_fsm_machine.rental_fsm_states.RENTAL_FSM_INPUT):
                status = rental_fsm_machine.error_types.SM_NO_ERROR
    else:
        status = rental_fsm_machine.error_types.SM_INVALID_INPUT
        print("Unsupported event type")
    # print("\t\t\t\t\t\trental_fsm_cal_validate(): Status {}".format(status))
    return status

'''
 * @brief State entry function
 *
 * This function is the entry function for current state. 
 *
 * @param machine - state machine identifier
 * @param currEvent   - event class (includes the event and also its type)
 *
 * @return standardized status code
'''
def rental_fsm_cal_entry(machine, currEvent):
    # print("rental_fsm_cal_entry()")
    status = rental_fsm_machine.error_types.SM_NO_ERROR
    machine.currState = rental_fsm_machine.rental_fsm_states.RENTAL_FSM_CAL;
    return status

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

'''
 * @brief General state exit function
 *
 * This function is the exit function for current state. 
 *
 * @param machine - state machine identifier
 * @param event  - event class (includes the event and also its type)
 *
 * @return standardized status code
'''
def rental_fsm_cal_exit(machine, currEvent):
    status = rental_fsm_machine.error_types.SM_NO_ERROR
    # print("rental_fsm_cal_exit(): event: ", currEvent)
    return status