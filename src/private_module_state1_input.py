'''
 * @file        private_module_input.py
 * @ingroup     src
 * @brief       Files containing internal/private APIs for the current state
 *
 * Contains definitions of APIs specific to the current state
 *
'''

from fsm_types import *
from fsm_api import *
from private_module_state1_impl import *

'''
 * @brief Validate the next state for current state
 *
 * This function is design to check that the requested state transition can be allowed for the current state.
 *
 * @param currEvent         - event
 * @param next_state    - next state to move to
 *
 * @return standardized status code
'''
def rental_fsm_input_validate(currEvent, next_state):
    # print("rental_fsm_input_validate()")
    # print("Debug: EventType: {}".format(currEvent.eventType))
    # print("Debug: Event: {}".format(currEvent.event))
    
    status = rental_fsm_machine.error_types.SM_INVALID_TRANSITION
   
    if(currEvent.eventType != event.rental_fsm_event_type.RENTAL_FSM_MSG):
        if( (currEvent.event == event.rental_fsm_event.SUCCEEDED) or (currEvent.event == event.rental_fsm_event.INIT) ):
            
            if(next_state == rental_fsm_machine.rental_fsm_states.RENTAL_FSM_CAL):
                status = rental_fsm_machine.error_types.SM_NO_ERROR
            
        elif(currEvent.event == event.rental_fsm_event.FAILED):
            
            if(next_state == rental_fsm_machine.rental_fsm_states.RENTAL_FSM_INPUT):
                status = rental_fsm_machine.error_types.SM_NO_ERROR
    else:
        status = rental_fsm_machine.error_types.SM_INVALID_INPUT
        print("Unsupported event type{}".format(currEvent.eventType))
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
def rental_fsm_input_entry(machine, currEvent):
    # print("rental_fsm_input_entry()")
    status = rental_fsm_machine.error_types.SM_NO_ERROR
    machine.currState = rental_fsm_machine.rental_fsm_states.RENTAL_FSM_INPUT;
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

'''
 * @brief Get Input State Object
 *
 * This function will return the object used for the current state from the shared memory. Most likely called for inter-state sharing
 *
 * @return object reference
'''
def get_input_state_obj_from_shared_mem():
    obj = sharedM.getInputObj()
    return (obj)

'''
 * @brief General state exit function
 *
 * This function is the exit function for current state. Add any cleanup work (if required)
 *
 * @param machine - state machine identifier
 * @param event   - event class (includes the event and also its type)
 *
 * @return standardized status code
'''
def rental_fsm_input_exit(machine, currEvent):
    status = rental_fsm_machine.error_types.SM_NO_ERROR
    # print("rental_fsm_input_exit(): event: ", currEvent)
    return status