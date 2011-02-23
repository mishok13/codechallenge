(ns greplin
  (:require clojure.string))


(defn palindrome? [^String string]
  (= string (clojure.string/reverse string)))


(defn words [string limit]
  (let [limit (int limit) string-length (count string)]
    (loop [length limit start 0 result '()]
      (if (> length string-length)
	result
	(if (>= (+ start length) string-length)
	  (recur (inc length) 0 (conj result (.substring string start (+ start length))))
	  (recur length (inc start) (conj result (.substring string start (+ start length)))))))))

(println (first (filter palindrome? (words (slurp "/home/mishok/Downloads/gettysburg.txt") 1))))
