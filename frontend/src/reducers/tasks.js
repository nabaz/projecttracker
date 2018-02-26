import * as echo from '../actions/tasks'

const initialState = {
  tasks: ""
}

export default (state=initialState, action) => {
  switch(action.type) {
    case echo.TASKS_SUCCESS:
      return {
        tasks: action.payload,
      }
    default:
      return state
  }
}

export const serverTasks = (state) => state.tasks
