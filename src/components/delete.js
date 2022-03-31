import React from 'react'

export const Delete = () => {
    const deleteComment = () => {
        fetch('http://172.29.128.254:8080/deleterates/', {
            method: 'POST',


        }).then(resp => resp.text())
            .then(data => {
                console.log(data)
            })
    }

    return (
        <>
            <button onClick={deleteComment}>Delete 1 Click Here!</button>
        </>
    )
}