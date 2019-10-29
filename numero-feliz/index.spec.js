const index = require('./index')

test('O 7 é feliz', function () {
    const efeliz = index.eFeliz(7)
    expect(efeliz).toBe(true)
})

test('8 não é feliz', function () {
    const efeliz = index.eFeliz(8)
    expect(efeliz).toBe(false)
})

test('9 não é feliz', function () {
    const efeliz = index.eFeliz(9)
    expect(efeliz).toBe(false)
})

test('10 é feliz', function () {
    const efeliz = index.eFeliz(10)
    expect(efeliz).toBe(true)
})