"use client";
import { TypewriterEffectSmooth } from "../components/ui/typewriter-effect";
export function TypewriterEffectSmoothDemo() {
  const words = [
     {
    text: "Interactive",
    className: "word-interactive",
  },
  {
    text: "Story",
    className: "word-interactive",
  },
  {
    text: "Generator",
    className: "word-generator",
  },
];
  return (
    <div className="flex  items-center justify-center  ">
    
      <TypewriterEffectSmooth   words={words} />
      
    </div>
  );
}
