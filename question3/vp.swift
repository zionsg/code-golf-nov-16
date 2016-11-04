class i : IteratorProtocol {
    var k:Int = 1
    func next() -> Int?{
        k = k % 2 ? pow(k, 1/2) : pow(k, 3/2)
        k
    }
}
