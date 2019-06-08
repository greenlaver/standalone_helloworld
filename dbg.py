import lldb

exe = "target/debug/hello"

dbg = lldb.SBDebugger.Create()
dbg.SetAsync(False)

dbg.HandleCommand("settings set target.source-map /rustc/3c235d5600393dfe6c36eeed34042efad8d4f26e/src/ /home/ubuntu/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/lib/rustlib/src/rust/src/")
dbg.HandleCommand('settings set frame-format frame "frame #${frame.index}: ${frame.pc}{ ${module.file.basename}{`${function.name-with-args}{${frame.no-debug}${function.pc-offset}}}}{ at ${line.file.fullpath}:${line.number}}{${function.is-optimized} [opt]}\n"')

target = dbg.CreateTarget(exe)
launch_info = lldb.SBLaunchInfo([exe])
breakpoint = target.BreakpointCreateBySourceRegex(
    'Hello, world!', lldb.SBFileSpec("main.rs"))
error = lldb.SBError()
process = target.Launch(launch_info, error)

dbg.HandleCommand("f")

thread = process.GetThreadAtIndex(0)
out = ""
while len(out) == 0 and process.GetState() != lldb.eStateExited:
    thread.StepInto()
    out = process.GetSTDOUT(1024)

dbg.HandleCommand("bt")
dbg.HandleCommand("f")

