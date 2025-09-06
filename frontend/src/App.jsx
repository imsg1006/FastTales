import './App.css'
import {BrowserRouter as Router , Route , Routes} from 'react-router-dom'
import StoryLoader from './components/StoryLoader'
import StoryGenerator from './components/StoryGenerator'
import { TypewriterEffectSmoothDemo } from './components/Heading'

function App() { 
  return (
     <Router>
      <div className='app-container'>
        <header> 
          <TypewriterEffectSmoothDemo/>
        </header>
        <main>
          <Routes>
            <Route path={"/story/:id"} element={<StoryLoader/>}/>
            <Route path={"/"} element={<StoryGenerator/>}/>
          </Routes>
        </main>
      </div>
     </Router>
  )
}

export default App
