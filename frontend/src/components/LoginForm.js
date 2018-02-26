import React, {Component} from 'react';
import { Alert, Jumbotron,  Form } from 'reactstrap';

import RaisedButton from 'material-ui/Button';
import TextField  from 'material-ui/TextField';

export default class LoginForm extends Component {
  state = {
    username: '',
    password: ''
  }

  handleInputChange = (event) => {
    const target = event.target;
    const value = target.type ===
        'checkbox' ? target.checked : target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  onSubmit = (event) => {
    event.preventDefault()
    this.props.onSubmit(this.state.username, this.state.password)
  }

  render() {
    const errors = this.props.errors || {}
    const style = {
      margin: 12,
    };

    return (
      <Jumbotron className="container">
        <Form onSubmit={this.onSubmit}>
          <h1>Login</h1>
          {errors.non_field_errors?<Alert color="danger">{errors.non_field_errors}</Alert>:""}
          <TextField name="username" label="Type username" error={errors.username} onChange={this.handleInputChange}/><br/>
          <TextField name="password" label="Password" error={errors.password} type="password" onChange={this.handleInputChange}/><br/>
          <RaisedButton type="submit" style={style} variant="raised" color="primary"> Login </RaisedButton>
        </Form>
      </Jumbotron>
    )
  }
}
