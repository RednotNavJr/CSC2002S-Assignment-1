/** 
 * @author Joshua van Tonder (VTNJOS003)
 */

class FireTask implements Runnable {
    private final FireMapParallel map;
    private final FireMapParallel.Mode mode;
    private final int startRow;
    private final int endRow;
    private final int startColumn;
    private final int endColumn;

    public FireTask(FireMapParallel map, FireMapParallel.Mode mode, int startRow, int endRow, int startColumn, int endColumn) {
        this.map = map;
        this.mode = mode;
        this.startRow = startRow;
        this.endRow = endRow;
        this.startColumn = startColumn;
        this.endColumn = endColumn;
    }

    @Override
    public void run() {
        map.updateRegion(mode, startRow, endRow, startColumn, endColumn);
    }
}