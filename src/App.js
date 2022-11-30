import './App.css';
import Header from './Components/Header/Header';
import Home from './Components/Pages/Home/Home';

function App() {
  return (
    <>
      <Header />

      <main className='main'>
        <Home />
      </main>
    </>
  );
}

export default App;
