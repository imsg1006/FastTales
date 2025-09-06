import { LoaderFiveDemo } from "./Load";

function LoadingStatus({theme}) {
    return <div className="loading-container">
        <h2>Generating Your {theme} Story</h2>

        <div className="loading-animation"> 
            <LoaderFiveDemo/>
        </div>
        <p className="loading-info">
            Please wait while we craft your story. This may take a few moments.
        </p>
    </div>
}

export default LoadingStatus;