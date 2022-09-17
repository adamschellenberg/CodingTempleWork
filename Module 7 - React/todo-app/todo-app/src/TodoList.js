import React from 'react'
import DataLoop from './DataLoop'

export default function TodoList({todos}) {
  return (
    <DataLoop todos={todos}/>
  )
}
