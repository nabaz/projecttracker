import React, { Component } from 'react';
import { connect, PromiseState } from 'react-refetcher';

class Customer extends Component {
  render(){
    const { customerFetch } = this.props

    if (customerFetch.pending) {
      return <lodingAnimation/>
    } else if (customerFetch.rejected) {
      return <Error error={customerFetch.reason}/>
   } else if (customerFetch.fulfilled) {
     return <Customer customer={customerFetch.value}/>
   }

  }
}

export default connect(props => ({
  customerFetch : `/customers`
}))(Customer)
