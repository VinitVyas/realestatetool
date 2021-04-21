'''
 * @file        print_apis.py
 * @ingroup     helpers
 * @brief       APIs to print data
 *
 * Contains definitions of APIs that print various details related to a state 
 *
'''

from fsm.types.fsm_types import *

# Global variables
sharedM_FSM = SharedMem_FSM()

'''
 * @brief Print the requested state 
 *
 * This function prints the value of the current state
 *
 * @param state   - state value to by printed
 *
 * @return standardized status code
'''

def printState(state):
    # print("printState()")
    status = rental_fsm_machine.error_types.SM_NO_ERROR

    if(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_INPUT    == state):
        print("\tState: RENTAL_FSM_INPUT")

    elif(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_CAL    == state):
        print("\tState: RENTAL_FSM_CAL")

    elif(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_PRINT  == state):
        print("\tState: RENTAL_FSM_PRINT")

    elif(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_END    == state):
        print("\tState: RENTAL_FSM_END")

    else:
        print("\tUnknown entry state")
        status = rental_fsm_machine.error_types.SM_INVALID_INPUT

    # print("\n")
    return status


'''
 * @brief Print the requested event 
 *
 * This function prints the value of the current event
 *
 * @param event   - event value to by printed
 *
 * @return standardized status code
'''

def printEventValue(currEventValue):
    # print("printEventValue()")
    status = rental_fsm_machine.error_types.SM_NO_ERROR

    if(event.rental_fsm_event.RENTAL_FSM_EVENT_UNKNOWN  == currEventValue):
        print("\tEventValue: RENTAL_FSM_EVENT_UNKNOWN")

    elif(event.rental_fsm_event.INIT        == currEventValue):
        print("\tEventValue: INIT")

    elif(event.rental_fsm_event.SUCCEEDED   == currEventValue):
        print("\tEventValue: SUCCEEDED")

    elif(event.rental_fsm_event.FAILED      == currEventValue):
        print("\tEventValue: FAILED")

    else:
        print("\tUnknown entry eventValue: {}".format(currEventValue))
        status = rental_fsm_machine.error_types.SM_INVALID_INPUT

    # print("\n")
    return status

'''
 * @brief Print the requested event type 
 *
 * This function prints the value of the current event type
 *
 * @param event   - event type value to by printed
 *
 * @return standardized status code
'''

def printEventType(currEventType):
    # print("printEventType()")
    status = rental_fsm_machine.error_types.SM_NO_ERROR

    if(event.rental_fsm_event_type.RENTAL_FSM_EVENT_TYPE_UNKNOWN  == currEventType):
        print("\tEventType: RENTAL_FSM_EVENT_TYPE_UNKNOWN")

    elif(event.rental_fsm_event_type.RENTAL_FSM_MSG      == currEventType):
        print("\tEventType: RENTAL_FSM_MSG")

    elif(event.rental_fsm_event_type.RENTAL_FSM_EVENT    == currEventType):
        print("\tEventType: RENTAL_FSM_EVENT")

    else:
        print("\tUnknown entry eventType: {}".format(currEventType))
        status = rental_fsm_machine.error_types.SM_INVALID_INPUT

    # print("\n")
    return status

'''
 * @brief Print the requested event type 
 *
 * This function prints the value of the current event type
 *
 * @param event   - event type value to by printed
 *
 * @return standardized status code
'''

def printEvent(currEvent):
    # print("printEvent()")
    
    # Print Event Type
    printEventType(currEvent.eventType)

    if(currEvent.eventType == event.rental_fsm_event_type.RENTAL_FSM_EVENT):
        printEventValue(currEvent.event)
    else:
        print("This Event Type is currently unsupported")
