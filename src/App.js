import logo from './logo.png';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          With you to the grave...
        </p>
        <a
          className="App-link"
          href="https://memorialbrooklyn.com/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Check out the site
        </a>
      </header>
    </div>
  );
}

export default App;
