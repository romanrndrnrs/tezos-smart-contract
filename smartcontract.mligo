(* Parameter *)

type parameter =
| Increment of int 
| Decrement of int 
| Multiply of int
| Divide of int
| Modulo of int
| Reset

(* Storage *)

type storage = int

(* Code *)

let add (storVal,n : storage*int) : storage = 
    storVal + n

let sub (storVal,n : storage*int) : storage = 
    storVal - n

let mult (storVal,n : storage*int) : storage = 
    storVal * n

let div (storVal,n : storage*int) : storage = 
    storVal / n

let mod_ (storVal,n : storage*int) : storage = 
    (* cast because the value returned by mod is a nat*)
    int (storVal mod n)


let main (p,s : parameter * storage) : operation list * storage = 
    let storage =
        match p with
        | Increment (n) -> add (s,n)
        | Decrement (n) -> sub (s,n)
        | Multiply (n) -> mult (s,n)
        | Divide (n) -> div (s,n)
        | Modulo (n) -> mod_ (s,n)
        | Reset -> 0
    in ([] : operation list),storage
