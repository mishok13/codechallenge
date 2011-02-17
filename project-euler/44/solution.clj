(defn pentagonal [index]
  (let [index (int index)]
    (/ (- (* 3 index index) index) 2)))


(defn condition?
  [j k]
  (let [j (int j) k (int k) sub (Math/abs (- (pentagonal j) (pentagonal k)))]
    (loop [i (min j k)]
      (if (= (pentagonal i) sub)
	true
	(if (<= i 1)
	  false
	  (recur (dec i)))))))


(defn cond-cached? [j k cache]
  (and (contains? cache (Math/abs (- (pentagonal j) (pentagonal k))))
       (contains? cache (+ (pentagonal j) (pentagonal k)))))


(defn solve [limit]
  (let [limit (int (* limit 3))]
    (loop [i 4 k 7 result '()]
      (if (> i limit)
	result
	(if (> k limit)
	  (recur (+ 3 i) (+ 6 i) result)
	  (if (condition? i k)
	    (recur i (+ 4 i) (cons result [i k]))
	    (recur i (+ 4 i) result)))))))


(defn solve-cached
  [limit start-step]
  (let [limit (int limit)
	start-step (int start-step)
	half-limit (Math/round (* (Math/log limit) (Math/sqrt limit)))
	cache (set (map pentagonal (range 1 (* 2 (inc limit)))))
	pentagonals (apply vector (map pentagonal (range 1 (inc limit))))]
    (loop [step start-step i 0 k start-step result '()]
      (if (>= step half-limit)
    	result
    	(if (>= k limit)
    	  (recur (inc step) 0 (inc step) result)
    	  (if (and (contains? cache (+ (nth pentagonals i) (nth pentagonals k)))
    		   (contains? cache (- (nth pentagonals k) (nth pentagonals i))))
    	    (recur step (inc i) (inc k)
		   (conj result [i k (nth pentagonals i) (nth pentagonals k)
				 (- (nth pentagonals k) (nth pentagonals i))]))
    	    (recur step (inc i) (inc k) result)))))))

(println (time (solve-cached 1000000 100)))
