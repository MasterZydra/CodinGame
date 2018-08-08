// The while loop represents the game.
// Each iteration represents a turn of the game
// where you are given inputs (the heights of the mountains)
// and where you have to print an output (the index of the mountain to fire on)
// The inputs you are given are automatically updated according to your last actions.
program Answer;
{$H+}
uses sysutils, classes, math;

// Helper to read a line and split tokens
procedure ParseIn(Inputs: TStrings) ;
var Line : string;
begin
    readln(Line);
    Inputs.Clear;
    Inputs.Delimiter := ' ';
    Inputs.DelimitedText := Line;
end;

var
    mountainH : Int32; // represents the height of one mountain.
    i : Int32;
    Inputs: TStringList;
    highestMountIdx: Int32;
    highestMountH: Int32;
begin
    Inputs := TStringList.Create;

    // game loop
    while true do
    begin
        highestMountH := 0;
        highestMountIdx := -1;
        for i := 0 to 7 do
        begin
            ParseIn(Inputs);
            mountainH := StrToInt(Inputs[0]);
            if mountainH > highestMountH then
            begin
                highestMountH := mountainH;
                highestMountIdx := i;
            end;
        end;

        // Write an action using writeln()
        // To debug: writeln(StdErr, 'Debug messages...');
        writeln(IntToStr(highestMountIdx)); // The index of the mountain to fire on.
        flush(StdErr); flush(output); // DO NOT REMOVE
    end;
end.