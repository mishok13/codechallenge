(ns greplin
  (:require clojure.string clojure.contrib.combinatorics))


(defn palindrome? [^String string]
  (= string (clojure.string/reverse string)))


(defn words [string initial-length]
  "Generate all possible words
  that are longer than 'initial-lenth' from a given string"
  (let [initial-length (int initial-length) string-length (count string)]
    (loop [length initial-length start 0 result '()]
      (if (> length string-length)
	result
	(if (>= (+ start length) string-length)
	  (recur (inc length) 0 (conj result (.substring string start (+ start length))))
	  (recur length (inc start) (conj result (.substring string start (+ start length)))))))))


(def text (slurp "gettysburg.txt"))

;; runs in 10 seconds
(println (first (filter palindrome? (words text 1))))
