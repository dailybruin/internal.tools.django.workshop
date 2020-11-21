import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import React from 'react'

class App extends React.Component {

  componentDidMount() {
    axios.post("http://localhost:5000/notes/create", 
      {
        title: "My Note", 
        body: "body"
      }
    ).then(
      function(data) {
        console.log(data);
      }
    ).catch(
      function(err){
        console.log(err);
      }
    )
  }

  create(title, body) {
    axios.post("http://localhost:5000/notes/create", 
      {
        title: title, 
        body: body
      }
    ).then(
      function(data) {
        console.log(data);
      }
    ).catch(
      function(err){
        console.log(err);
      }
    )
  }

  update(id, title, body) {
    axios.put("http://localhost:5000/notes/update/" + id, 
      {
        title: title, 
        body:  body
      }
    ).then(
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
      <div> 
      <input type="text"  onChange={(event) => this.setState({"title": event.target.value})} />
      <input type="text" onChange={(event) => this.setState({"body": event.target.value}) } />
      <button onClick={() => this.update(2, this.state.title, this.state.body)}> click me </button>

      </div>
    );
  }
}

export default App;
