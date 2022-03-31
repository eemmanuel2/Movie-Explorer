
import React, { useState } from 'react'

export const Form = ({ userInput, onFormChange, handleFormSubmit }) => {
    const handleChange = (event) => {
        onFormChange(event.target.value)
    }

    const handleSubmit = (event) => {
        event.preventDefault()
    }
    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type='text' value={userInput} onChange={handleChange}></input>
                <input type='submit'></input>
            </form>
        </div>
    )
}

export default Form