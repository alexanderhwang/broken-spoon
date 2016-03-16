#lang racket

(define (max-num lst)

  (define head (car lst))
  (cond ((= 1 (length lst)) head)
        (else (define next (cadr lst))
              (if (> next head)
                  (max-num (cons next (cddr lst)))
                  (max-num (cons head (cddr lst))))))
)
  
;; The function counts from 1 to the specified number, returning a string with the result.
;; The rules are:
;;    If a number is divisible by 3 and by 5, instead say "fizzbuzz"
;;    Else if a number is divisible by 3, instead say "fizz"
;;    Else if a number is divisible by 5, instead say "buzz"
;;    Otherwise say the number
(define (fizzbuzz n)
  (println (fizzbuzz1 1 n)))

;; Helper function for fizzbuzz
(define (fizzbuzz1 i n)

  (if (> n 1)
      (string-append (fizzbuzz1 (+ i 1) (- n 1))
  
            (cond ((= 0 (modulo n 15)) " fizzbuzz")
                  ((= 0 (modulo n 5)) " buzz")
                  ((= 0 (modulo n 3)) " fizz")
                  (else (string-append " " (number->string n)))))
      (string-append "1"))
  
)

(max-num '(1 2 3 4 5))
(max-num '(-5 -3 -2 -13))
(max-num '(0 99 -5 100 101 94 -102 1))
(max-num '(6 6 -6 5 6))
(fizzbuzz 21)
(fizzbuzz 22)
