import React from 'react'
import { connect } from 'react-redux'
import { Redirect } from 'react-router'

import LoginForm from '../components/LoginForm'
import {login} from  '../actions/auth'
import {authErrors, isAuthenticated} from '../reducers'
import Paper from 'material-ui/Paper';

const style = {
  padding: 50,
  textAlign: 'center',
  display: 'inline-block',
};

const Login = (props) => {
  if(props.isAuthenticated) {
     return  <Redirect to='/' />
  }

  return (
     <div className="login-page">
        <Paper style={style}>
          <LoginForm {...props}/>
        </Paper>
    </div>
  )
}

const mapStateToProps = (state) => ({
  errors: authErrors(state),
  isAuthenticated: isAuthenticated(state)
})

const mapDispatchToProps = (dispatch) => ({
  onSubmit: (username, password) => {
    dispatch(login(username, password))
  }
})

export default connect(mapStateToProps, mapDispatchToProps)(Login);
