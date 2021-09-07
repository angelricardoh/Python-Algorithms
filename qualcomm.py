void ComputeHist (int [][] image, int height, int width) {
    int []histogram = new int(255);
    for (int i=0; i<=255; )
    // init
    
    for (int i=0; i<=height; i++) {
        for (int j=0; j<=width; j++) {
            int value = image[i][j];
            histogram[value] += 1; 
        }
    }    
}

void PrintHist (int [] hist, int max) {
    for (i=max; i>=0; i--) {
        for (int j=0; j<=hist.length; j++) {
            if (hist[j] == i) {
                print("*");
                hist[j] -= 1;
            } else {
                print(" ");
            }
            print("/t");
        }
    } 
    
    for (int j=0; j<=hist.length; j++) {
        print("%d", j);
        print("/t");
    }
}

#                 *
#                 *
#                 *       *
#                 *       *
#         *       *       *
#         *       *       *       *
# *       *       *       *       *
# 1       3       7       5       2

# 0       1       2       3