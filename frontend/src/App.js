import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import React from 'react'

class App extends React.Component {

  componentDidMount() {
    axios.get("http://localhost:5000/notes/hello_world").then(
      function(data) {
        console.log(data);
      }
    ).catch(
      function(err){
        console.log(err);
      }
    )
  }

  render() {
    return (
      <div> </div>
    );
  }
}

export default App;
