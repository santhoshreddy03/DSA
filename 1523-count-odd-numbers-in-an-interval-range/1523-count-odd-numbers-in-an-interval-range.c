int countOdds(int low, int high) {
    int x = (high - low )/ 2;
    if(((high % 2 )== 0 ) && ((low % 2) == 0)){
        return x;
    }
    return x + 1;
}