import { RSAA } from 'redux-api-middleware';
import { withAuth } from '../reducers'

export const TASKS_REQUEST = '@@tasks/TASKS_REQUEST';
export const TASKS_SUCCESS = '@@tasks/TASKS_SUCCESS';
export const TASKS_FAILURE = '@@tasks/TASKS_FAILURE';

export const tasks = (task) => ({
  [RSAA]: {
      endpoint: '/api/tasks/',
      method: 'GET',
      // body: JSON.stringify({name: 'nabaz', email:'email@test.com', note: 'dew', phone:'0987665555', address: '1234 sdfsd', web_url: 'adasdasdas', active: true}),
      headers: withAuth({ 'Content-Type': 'application/json' }),
      types: [
        TASKS_REQUEST, TASKS_SUCCESS, TASKS_FAILURE
      ]
  }
})
