"use client";
import { TypewriterEffectSmooth } from "../components/ui/typewriter-effect";
export function TypewriterEffectSmoothDemo() {
  const words = [
    {
      text: "Interactive",
      className:"text-pink-400  "
    },
    {
      text: "Story",
      className:"text-pink-400 mr-5"
    },
    {
      text: "Generator",
      className: "text-purple-500 dark:text-blue-500"
    },
     
  ];
  return (
    <div className="flex flex-col items-center justify-center  ">
    
      <TypewriterEffectSmooth className="word-spacing" words={words} />
      
    </div>
  );
}
