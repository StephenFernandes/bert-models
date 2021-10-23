mport "./App.css";
import HomePage from "./Components/HomePage";

const newFunction = () => {
  console.log("Stallone Fernandes");
};

//Function Called 
newFunction();
console.log("Another Pull Request Made");

function App() {
  return (
    <div className="App">
      <HomePage></HomePage>
    </div>
  );
}

export default App;
