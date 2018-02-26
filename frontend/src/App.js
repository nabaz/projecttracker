import React, { Component } from 'react';
import { connect } from 'react-redux'
import { tasks } from './actions/tasks'
import { serverTasks } from './reducers'
class App extends Component {
  componentDidMount() {
      this.props.fetchMessage('Hi!')
  }
render() {
    return (
      <div>
        <h2>Welcome to the Demo</h2>
        <p><a href="/customers" > Customers</a></p>
        <p><a href="/projects" > Projects</a></p>
        <p><a href="/tasks" > Task</a></p>
        <p><a href="/time-entries" > Time Entry</a></p>
      </div>
    );
  }
}
export default connect(
  state => ({ message: serverTasks(state) }),
  { fetchMessage: tasks }
)(App);
