function go(textInput) {
    const input = textInput.split('\n').map(n => parseInt(n, 10));
    return input.reduce((sum, e, i) => {
        if (i < 3) return sum;
        const curr = e + input[i-1] + input[i-2];
        const prev = input[i-1] + input[i-2] + input[i-3];
        console.log({curr, prev});
        if (curr > prev) return sum+1;
        return sum;
    }, 0);
}
