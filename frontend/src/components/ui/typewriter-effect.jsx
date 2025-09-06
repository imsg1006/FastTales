"use client";

import { cn } from "../../lib/utils";
import { motion, stagger, useAnimate, useInView } from "framer-motion";
import { useEffect } from "react";

export const TypewriterEffect = ({ words, className, cursorClassName }) => {
  const wordsArray = words.map((word) => {
    return { ...word, text: word.text.split(" ") };
  });

  const [scope, animate] = useAnimate();
  const isInView = useInView(scope);

  useEffect(() => {
    if (isInView) {
      animate(
        "span",
        {
          display: "inline-block",
          opacity: 1,
          width: "fit-content",
        },
        {
          duration: 0.3,
          delay: stagger(0.1),
          ease: "easeInOut",
        }
      );
    }
  }, [isInView]);

  const renderWords = () => (
    <motion.div ref={scope} className="inline">
      {wordsArray.map((word, idx) => (
        <span key={`word-${idx}`} className="inline-block mr-2">
          {word.text.map((char, index) => (
            <motion.span
              initial={{}}
              key={`char-${index}`}
              className={cn(word.className)}
            >
              {char}
            </motion.span>
          ))}
        </span>
      ))}
    </motion.div>
  );

  return (
    <div className={cn("typewriter-container", className)}>
      {renderWords()}
      <motion.span
        initial={{ opacity: 0 }}
        className={cn("typewriter-cursor", cursorClassName)}
      />
    </div>
  );
};

export const TypewriterEffectSmooth = ({ words, className, cursorClassName }) => {
  // split into characters but add a space explicitly at the end of each word
  const wordsArray = words.map((word, idx) => {
    return {
      ...word,
      text: [...word.text.split(""), " "], // 👈 ensures spacing
    };
  });

  const renderWords = () => (
    <div>
      {wordsArray.map((word, idx) => (
        <span key={`word-${idx}`} className="inline-block">
          {word.text.map((char, index) => (
            <span
              key={`char-${index}`}
              className={cn("text-dark", word.className)}
            >
              {char}
            </span>
          ))}
        </span>
      ))}
    </div>
  );

  return (
    <div className={cn("typewriter-smooth-container", className)}>
      <motion.div
        className="overflow-hidden"
        initial={{ width: "0%" }}
        whileInView={{ width: "fit-content" }}
        transition={{ duration: 2, ease: "linear", delay: 1 }}
      >
        <div className="typewriter-smooth-text">{renderWords()}</div>
      </motion.div>
      <motion.span
        initial={{ opacity: 0 }}
        className={cn("typewriter-smooth-cursor", cursorClassName)}
      />
    </div>
  );
};
