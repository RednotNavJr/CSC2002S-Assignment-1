/** 
 * @author Joshua van Tonder (VTNJOS003)
 */

import java.util.concurrent.RecursiveTask;

class FireTask extends RecursiveTask<FireMapParallel.StepResult> {
    private final FireMapParallel map;
    private final FireMapParallel.Mode mode;
    private final int sequentialCutoff;
    private final int startRow;
    private final int endRow;
    private final int startColumn;
    private final int endColumn;

    public FireTask(FireMapParallel map, FireMapParallel.Mode mode, int SequentialCutoff, int startRow, int endRow, int startColumn, int endColumn) {
        this.map = map;
        this.mode = mode;
        this.sequentialCutoff = SequentialCutoff;
        this.startRow = startRow;
        this.endRow = endRow;
        this.startColumn = startColumn;
        this.endColumn = endColumn;
    }

    @Override
    public FireMapParallel.StepResult compute() {

        if (endRow - startRow <= sequentialCutoff) {
            
            return map.updateRegion(mode, startRow, endRow, startColumn, endColumn);

        } else {
            
            int midRow = (startRow + endRow) / 2;

            FireTask topHalf = new FireTask(map, mode, sequentialCutoff, startRow, midRow, startColumn, endColumn);
            FireTask bottomHalf = new FireTask(map, mode, sequentialCutoff, midRow, endRow, startColumn, endColumn);

            topHalf.fork();
            FireMapParallel.StepResult bottomResult = bottomHalf.compute();
            FireMapParallel.StepResult topResult = topHalf.join(); 

            return FireMapParallel.StepResult.combine(topResult, bottomResult);
        }
        
    }

}