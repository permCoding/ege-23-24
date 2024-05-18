
console.log(
    Array(parseInt(10_000_000, 7) - parseInt(1_000_000, 7))
        .fill(parseInt(1_000_000, 7))
        .map((e, i) => (e + i).toString(7).split('').map(e => +e).filter(e => e % 2 === 0).length === 2)
        .filter(e => e)
        .length
)