import React, { useEffect, useState } from 'react';
import './App.css';
import { Form } from './form';
import { Delete } from './components/delete';
function App() {
  const [comments, setComments] = useState([])
  const [addcomments, setaddcomments] = useState("")

  useEffect(() => {
  }, []
  )





  fetch('/getrates/', {
    'methods': 'GET',
    headers: {
      'Content-Type': 'applications/json'
    }

  }
      ,)


    .then(resp => resp.text())
    .then(resp => setComments(resp))
    .catch(error => console.log(error))




  const handleFormChange = (inputValue) => {
    setaddcomments(inputValue)
    console.log(addcomments)
  }

  const handleFormSubmit = () => {
    fetch('/deleterates/', {
      'methods': 'POST',
      body: JSON.stringify({
        content: addcomments
      }),
      headers: {
        'Content-Type': 'applications/json'
      }
    }).then(resp => resp.text())
      .then(message => console.log(message))
    setaddcomments("")
  }




  return (
    <div className="App">
      <header className="App-header">

        <p>MAKE SURE TO REFRESH PAGE TO SEE THE UPDATE... 1 CLICK 1 DELETE </p>
        <Form userInput={addcomments} onFormChange={handleFormChange} onFormSubmit={handleFormSubmit} />
        <br></br>
        <ol>{comments}

        </ol>
        <br></br>
        <Delete onFormChange={handleFormChange} onFormSubmit={handleFormSubmit} />
        <div className="col">

        </div>


      </header>
    </div >

  );
}

export default App;

