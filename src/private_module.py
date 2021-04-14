'''
 * @file        private_module.py
 * @ingroup     src
 * @brief       Files containing internal/private APIs
 *
 * Contains definitions of private APIs
 *
'''

from fsm_types import *
from fsm_api import *
from private_module_state1_input import *
from private_module_state2_cal import *
from private_module_state3_print import *
from private_module_state4_end import *

'''
 * @brief General state entry function
 *
 * This function is the general state entry function. It should be invoked when entering a new state.
 * The function calls the state-specific entry function
 *
 * @param machine - state machine identifier
 * @param currEvent   - event class (includes the event and also its type)
 *
 * @return standardized status code
'''
def rental_fsm_entry(machine, currEvent):
    # print("rental_fsm_entry()")
    status = rental_fsm_machine.error_types.SM_NO_ERROR

    # printState(machine.currState);

    if(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_INPUT    == machine.currState):
        status = rental_fsm_input_entry(machine, currEvent)

    elif(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_CAL    == machine.currState):
        status = rental_fsm_cal_entry(machine, currEvent)

    elif(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_PRINT  == machine.currState):
        status = rental_fsm_print_entry(machine, currEvent)

    # elif(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_END    == machine.currState):
        # status = rental_fsm_end_entry(machine, currEvent)

    else:
        print("Unknown entry state")
        status = rental_fsm_machine.error_types.SM_INVALID_INPUT

    return status

'''
 * @brief General state exit function
 *
 * This function is the exit function. It should be invoked when exiting a state.
 * The function calls the state-specific exit function
 *
 * @param machine - state machine identifier
 * @param currEvent   - event class (includes the event and also its type)
 *
 * @return standardized status code
'''
def rental_fsm_exit(machine, currEvent):
    # print("rental_fsm_exit()")
    status = rental_fsm_machine.error_types.SM_NO_ERROR;
    
    if(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_INPUT == machine.prevState):
        status = rental_fsm_input_exit(machine, currEvent)

    elif(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_CAL == machine.prevState):
        status = rental_fsm_cal_exit(machine, currEvent)

    elif(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_PRINT == machine.prevState):
        status = rental_fsm_print_exit(machine, currEvent)

    # elif(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_END == machine.prevState):
        # status = rental_fsm_end_exit(machine, currEvent)

    else:
        print("Unknown exit state")
        status = rental_fsm_machine.error_types.SM_INVALID_INPUT;

    return status

'''
 * @brief State transition function
 *
 * This function is called when transitioning from one state to another.
 *
 * @param machine       - state machine identifier
 * @param next_state    - next state to move to
 * @param currEvent         - event class (includes the event and also its type)
 *
 * @return standardized status code
'''
def rental_fsm_transition(machine, next_state, currEvent):
    # print("rental_fsm_transition():")    
    # print("\n************ FSM Transition ************")
    # printState(machine.currState);
    # print("\t\t to ")
    # printState(next_state)
    # printEvent(currEvent)
    # print("****************************************\n")

    machine.transitionStatus = rental_fsm_validate_state_transition(machine.currState, currEvent, next_state)
    if (machine.currState != next_state):

        if (machine.transitionStatus == rental_fsm_machine.error_types.SM_NO_ERROR):
            machine.currState = next_state
            rental_fsm_exit(machine, currEvent)

        else:
            print("rental_fsm_transition(): Invalid State Transition")
            printState(machine.currState);
            print("\t\t to ")
            printState(next_state)
            printEvent(currEvent)
            print("\ttransitionStatus: {}".format(machine.transitionStatus))
    # print("\t\trental_fsm_transition(): machine.transitionStatus {}".format(machine.transitionStatus))
    return(machine.transitionStatus)

'''
 * @brief Validate a state transition
 *
 * This function is design to check that the requested state transition can be allowed.
 *
 * @param machine       - state machine identifier
 * @param next_state    - next state to move to
 *
 * @return standardized status code
'''
def rental_fsm_validate_state_transition(currState, event, next_state):
    # print("rental_fsm_validate_state_transition()")
    status = rental_fsm_machine.error_types.SM_INVALID_TRANSITION;

    if(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_INPUT == currState):
        status = rental_fsm_input_validate(event, next_state)
    
    elif(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_CAL == currState):
        status = rental_fsm_cal_validate(event, next_state)
    
    elif(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_PRINT == currState):
        status = rental_fsm_print_validate(event, next_state)

    # elif(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_END == currState):
        # status = rental_fsm_end_validate(event, next_state)

    else:
        print("Unknown state for transition")
        status = rental_fsm_machine.error_types.SM_INVALID_TRANSITION;

    return status

'''
 * @brief Kill the current process
 *
 * This function is design to work in a multi-core environment with multiple threads.
 * This API would be executed in the thread/task context and kill the allocated memory.
 * For single thread application, this is a no-op
 *
 * @param machine       - state machine identifier
 *
 * @return standardized status code
'''
def rental_fsm_kill_process(machine):
    # print("rental_fsm_kill_process")
    ''' No-Op for single thread '''
    status = rental_fsm_machine.error_types.SM_NO_ERROR
    return status