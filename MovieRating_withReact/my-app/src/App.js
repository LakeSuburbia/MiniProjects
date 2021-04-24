
import './App.css';


const Intro = (props) => (
  <p className="App-intro">
    Our first functional components
    </p>
)

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 className="App-title">
          TV Series List
        </h1>
      </header>
      <Intro />
    </div>
  );
}

export default App;
