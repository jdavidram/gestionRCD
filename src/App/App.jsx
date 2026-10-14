import logo from './logo.svg';
import { Colibri } from '@mteherandev/colombia-icons-react';
import './App.scss';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Colibri size={24} color="#61dafb" className='App-logo' />
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
