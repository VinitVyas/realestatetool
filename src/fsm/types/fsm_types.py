'''
 * @file        fsm_types.py
 * @ingroup     types
 * @brief       User defined datatypes for FSM
 *
 * Contains definitions of types including error codes, state & event definitions
 *
'''


'''
 * @brief Define Event Class
'''
class event:

    '''################## class API ##################'''
    def __init__(self): 
        ## Instantiating the 'rental_fsm_event_type' class
        self.eventType   = self.rental_fsm_event_type()
        ## Instantiating the 'rental_fsm_event' class
        self.event       = self.rental_fsm_event()

    def show_classes(self):
        # print("This is the event class")
        print(eventType)
        print(event)

    '''################## Subclasses ##################'''
    '''
     * @brief RENTAL_FSM event subclass
    '''
    class rental_fsm_event_type:
        RENTAL_FSM_EVENT_TYPE_UNKNOWN = 0  # Unknown or undefined event code
        RENTAL_FSM_MSG      = 1            # Message event
        RENTAL_FSM_EVENT    = 2            # Regular Event
        RENTAL_FSM_NUM_EVENT_TYPES    = 3  # Number of events

    class rental_fsm_event:
        RENTAL_FSM_EVENT_UNKNOWN = 0       # Unknown or undefined event code
        INIT        = 1
        SUCCEEDED   = 2    
        FAILED      = 3
        RENTAL_FSM_NUM_EVENTS = 4          # Number of events


'''
 * @brief RENTAL_FSM State Machine Type
'''
class rental_fsm_machine:
    ''' ###### class API ###### '''
    def __init__(self): 
        ## Instantiating the 'prevState' class
        self.prevState    = self.rental_fsm_states()    # Previous state of machine

        ## Instantiating the 'currState' class
        self.currState    = self.rental_fsm_states()    # Current state of machine
        self.eventType = event.rental_fsm_event_type()  # Event type
        self.event = event.rental_fsm_event()           # Actual event value

        ## Instantiating the 'transitionStatus' class
        self.transitionStatus = self.error_types()      # Status of last transition attempt
        self.parentCtx = 0                              # Parent context that this machine inst is a member of
        self.isProcessing = False                       # Flag indicating if the this machine is already processing

    def display(self):
        # print("This is the rental_fsm_machine class")
        print(prevState)
        print(currState)
        print(eventType)
        print(event)
        print(transitionStatus)
        print(parentCtx)
        print(isProcessing)

    '''
     * @brief RENTAL_FSM State class
    '''
    class rental_fsm_states:
        RENTAL_FSM_INVALID_STATE = 0    # Invalid state always defined as 0

        # Active states
        RENTAL_FSM_INPUT  = 1           # State RENTAL_FSM_INPUT
        RENTAL_FSM_CAL    = 2           # State RENTAL_FSM_CAL
        RENTAL_FSM_PRINT  = 3           # State RENTAL_FSM_PRINT
        RENTAL_FSM_END    = 4           # State RENTAL_FSM_END
        # Add additional states above this line

        RENTAL_FSM_NUM_STATES = 5      # Number of Active Stream FSM states

    class error_types:
        SM_INVALID_ERR_TYPE     = 0     # Invalid type

        # Active types
        SM_NO_ERROR             = 1     # Success notification
        SM_INVALID_INPUT        = 2     # Parameter is beyond the expected value range
        SM_ERROR                = 3     # Generic Error
        SM_INVALID_TRANSITION   = 4     # Invalid state transition
        SM_PROCESS_ERROR        = 5
        # Add additional error states above this line

        SM_NUM_ERROR_TYPES  = 6         # Number of error supported states


'''
 * @brief Shared memory data
'''
class SharedMem_FSM:
    ''' ###### class API ###### '''
    def __init__(self):
        self.machine = rental_fsm_machine()
    
    def getFSMObject(self):
        return(self.machine)

    def display(self):
        # print("This is the rental_fsm_machine class")
        print(machine)