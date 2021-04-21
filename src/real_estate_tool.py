'''
 * @file        real_estate_tool.py
 * @ingroup     src
 * @brief       Files containing external/public APIs
 *
 * Contains definitions of public APIs
 *
'''

from fsm.types.fsm_types import *
from fsm.helpers.fsm_apis import *
from fsm.states.input.public_apis import *
from fsm.states.cal.public_apis import *
from fsm.states.print.public_apis import *

'''
 * @brief State initialization function
 *
 * This function is called to initialize the state machine to the starting state.
 *
 * @param machine   - state machine
 * @param parentCtx - parent ctx that initiated this FSM
 *
 * @return standardized status code
'''
def rental_fsm_init(machine, parentCtx):
    # print("rental_fsm_init()")
    if (machine == None or parentCtx == None):
        print("rental_fsm_init(): Parent context not provided.")
        return rental_fsm_machine.error_types.SM_INVALID_INPUT

    machine.isProcessing     = False
    machine.transitionStatus = rental_fsm_machine.error_types.SM_NO_ERROR
    machine.parentCtx        = parentCtx
    machine.eventType        = event.rental_fsm_event_type.RENTAL_FSM_NUM_EVENT_TYPES
    machine.event            = event.rental_fsm_event.RENTAL_FSM_NUM_EVENTS
    machine.currState        = rental_fsm_machine.rental_fsm_states.RENTAL_FSM_INPUT
    machine.prevState        = rental_fsm_machine.rental_fsm_states.RENTAL_FSM_INVALID_STATE

    return rental_fsm_machine.error_types.SM_NO_ERROR;

'''
 * @brief Main process function
 *
 * This function is called to process a state machine. It will be called from outside the machine.
 *
 * @param machine - state machine identifier
 * @param event   - event class (includes the event and also its type)
 *
 * @return standardized status code
'''
def rental_fsm_process(machine, currEvent):
    # print("rental_fsm_process()")
    status = rental_fsm_machine.error_types.SM_ERROR;
    next_state = rental_fsm_machine.rental_fsm_states.RENTAL_FSM_INVALID_STATE;

    if (machine == None):
        ERROR("rental_fsm_process(): machine is NULL");
        return rental_fsm_machine.error_types.SM_INVALID_INPUT;

    if (machine.isProcessing):
        ERROR("rental_fsm_process(): machine is already processing");
        return rental_fsm_machine.error_types.SM_ERROR;

    machine.isProcessing = True;

    # If new to this state, run the entry function
    if (machine.currState != machine.prevState):
        rental_fsm_entry(machine, currEvent);    
    # print("After rental_fsm_entry")

    # Regardless, set the last state to the current state
    machine.prevState = machine.currState;

    if(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_INPUT == machine.currState):
        (status, next_state, eventVal) = rental_fsm_input_process(machine, currEvent)
        # print(status, next_state, eventVal)

    elif(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_CAL == machine.currState):
        (status, next_state, eventVal) = rental_fsm_cal_process(machine, currEvent)
        # print(status, next_state, eventVal)

    elif(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_PRINT == machine.currState):
        (status, next_state, eventVal) = rental_fsm_print_process(machine, currEvent)
        # print(status, next_state, eventVal)

    # elif(rental_fsm_machine.rental_fsm_states.RENTAL_FSM_END == machine.currState):
        # (status, next_state, eventVal) = rental_fsm_end_process(machine, currEvent)
        # print(status, next_state, eventVal)

    else:
        print("Unknown process state")
        status = rental_fsm_machine.error_types.SM_INVALID_INPUT
        next_state = rental_fsm_machine.rental_fsm_states.RENTAL_FSM_INVALID_STATE

    # FSM state transition logic (including exit state handler execution) must safe for re-entrant execution.
    machine.isProcessing = False;

    if(status == rental_fsm_machine.error_types.SM_NO_ERROR):
        # Transition to next state depending on process function return
        status = rental_fsm_transition(machine, next_state, currEvent);

    currEvent.rental_fsm_event = eventVal
    return (status, currEvent);

'''
 * @brief Get the parent context
 *
 * This function returns the parent context of a state machine.
 *
 * @param machine - state machine identifier
 *
 * @return parent context of the state machine
'''
def rental_fsm_get_parent_ctx(machine):
    # print("rental_fsm_get_parent_ctx()")
    if (machine == None):
        print("rental_fsm_get_parent_ctx(): machine is NULL");
        return None;

    return machine.parentCtx;

'''
 * @brief Get the state
 *
 * This function returns the current state of a state machine.
 *
 * @param machine - state machine identifier
 *
 * @return current state of the state machine
'''
def rental_fsm_get_state(machine):
    # print("rental_fsm_get_state()")
    if (machine == None):
        print("rental_fsm_get_state(): machine is NULL\n");
        return rental_fsm_machine.rental_fsm_states.RENTAL_FSM_INVALID_STATE;

    return machine.currState;

if __name__ == "__main__":
    # Variables
    status = rental_fsm_machine.error_types.SM_NO_ERROR

    # Carve out memory for FSM metadata
    machine = sharedM_FSM.getFSMObject()
    
    # Initialize the parentCtx to 0 (for a single threaded version)
    parentCtx = 0
    
    # Set event class to init
    currEvent = event()
    currEvent.eventType = event.rental_fsm_event_type.RENTAL_FSM_EVENT
    currEvent.event     = event.rental_fsm_event.INIT
    
    # Initialize the FSM
    rental_fsm_init(machine, parentCtx)
    #print("machine.parentCtx", machine.parentCtx)


    ''' ************ Process the state machine ************ '''
    while( (machine.currState < rental_fsm_machine.rental_fsm_states.RENTAL_FSM_END) and (status == rental_fsm_machine.error_types.SM_NO_ERROR) ):
        # Process the FSM
        (status, currEvent) = rental_fsm_process(machine, currEvent)
        # print("\t\t\t\t\t\tMain(): Status {}".format(status))
    ''' ************ FSM processing ends ************ '''


    # End process
    killStatus = rental_fsm_kill_process(machine)
    if(rental_fsm_machine.error_types.SM_NO_ERROR != killStatus):
        # This tbd with SMP. Currently a no-op
        print("Error with process kill")

    ''' End of API '''