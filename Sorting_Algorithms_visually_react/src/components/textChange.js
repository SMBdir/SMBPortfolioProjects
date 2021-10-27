import {Component} from 'react'

class textChange extends Component {
    constructor() {
       super();
       this.state =  {
          text: "Text to change",
       }
    }
 
    changeTitle = () => {
       this.setState({ title: "Great Success!" });
    };
 
    render() {
        return <h1 onClick={this.changeTitle}>{this.state.title}</h1>;
    }
 }