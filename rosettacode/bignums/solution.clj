(defn exp [n k]
  (cond
    (zero? (mod k 2)) (recur (* n n) (/ k 2))
    (zero? (mod k 3)) (recur (* n n n) (/ k 3))
    :else (reduce * (repeat k n))))

(def big (->> 2 (exp 3) (exp 4) (exp 5)))
(def sbig (str big))

(assert (= "62060698786608744707" (.substring sbig 0 20)))
(assert (= "92256259918212890625" (.substring sbig (- (count sbig) 20))))
(println (.substring sbig 0 20) "..."  (count sbig) (.substring sbig (- (count sbig) 20)) "digits")
