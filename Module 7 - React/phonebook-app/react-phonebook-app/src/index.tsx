import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { FirebaseAppProvider, AuthCheck} from 'reactfire';
import './style.css';
import { Home, Contact, About, Phonebook, SignIn } from './components';
import { firebaseConfig } from './firebaseConfig';
import 'firebase/auth';
import { Provider } from 'react-redux';
import { store } from './redux/store';

let myTitle = "Adam's Phonebook"

ReactDOM.render(
  <React.StrictMode>
    <FirebaseAppProvider firebaseConfig={firebaseConfig} suspense={true}>
    <Provider store={store}>
      <Router >
        <Switch>

          <Route exact path="/">
            <Home title={myTitle}/>
          </Route>
          <Route exact path="/phonebook">
            <Phonebook></Phonebook>
          </Route>
          <Route exact path="/contact">
            <Contact></Contact>
          </Route>
          <Route exact path="/about">
            <About></About>
          </Route>
          <Route exact path="/signin">
            <SignIn></SignIn>
          </Route>

        </Switch>
      </Router>
    </Provider>
    </FirebaseAppProvider>
  </React.StrictMode>,
  document.getElementById('root')
);