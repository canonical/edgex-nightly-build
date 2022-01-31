# edgex-sync

Canonical publishes a number of [EdgeX snaps](https://snapcraft.io/search?q=edgex) to the Snap Store. 

Daily builds are done from the [upstream](https://www.github.com/edgexfoundry) repositories.

This `edgex-sync` repository contains a number of Github Workflows which run once a day. They do the following:

## Workflow stages

### 1. Build the snap from the upstream sources

This stage builds the snap. It's stored as an artifact, which can be retrieved by clicking on the test run in the [Actions tab](https://github.com/canonical/edgex-sync/actions). 

The [snapcore/action-build](https://github.com/snapcore/action-build) Github Action is used to build the snap.
In case of failure a message is sent to the EdgeX tean on a channel on Canonical's Mattermost server. 

```
  build-snap:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v2
      with:
        repository: edgexfoundry/edgex-go
        fetch-depth: 0
        ref: main
    - name: Build the snap
      uses: snapcore/action-build@v1
    - name: Uploading snap artifact
      uses: actions/upload-artifact@v2
      with:
        name: snap-files
        path: "*.snap"   
    - name: MM Failure
      if: ${{ failure() }}
      run: |
        curl -i -X POST -H 'Content-Type: application/json' -d '{"username" : "github-builds", "text" : "<!channel> :warning: Build failed [${{github.event_name}}] ${{github.workflow}} [See logs](https://github.com/canonical/edgex-sync/actions/runs/${{github.run_id}}) "}' ${{secrets.MATTERMOST}}
  ```




### 2. (Optional) Test the snap

This basic sanity check tries to install the snap and sends a message if that fails. This stage only runs for the `edgexfoundry` snap.

```
    needs: build-snap
    steps:
    - name: testing snap install
      uses: actions/download-artifact@v2
      with:
        name:  snap-files
    - shell: bash 
      run: |
        sudo snap install --dangerous *.snap
    - name: MM Failure
      if: ${{ failure() }}
      run: |
        curl -i -X POST -H 'Content-Type: application/json' -d '{"username" : "github-builds", "text" : "<!channel> :warning: Test failed [${{github.event_name}}] ${{github.workflow}} [See logs](https://github.com/canonical/edgex-sync/actions/runs/${{github.run_id}}) "}' ${{secrets.MATTERMOST}}
```



### 3. Kick off build on Launchpad

If the above stages are succesful, then a build is kicked off on Launchpad, using a recipe which will publish the snap to the latest/edge channel.

```
  build-launchpad:
    runs-on: ubuntu-latest
    needs: test-snap
    steps:
      - name: Kick off Launchpad build
        uses: canonical/edgex-launchpad-build-action@v1.4
        with:
          edgex_snap: "edgexfoundry"
          consumer_name: ${{ secrets.LP_CONSUMER_NAME }}
          access_token: ${{ secrets.LP_ACCESS_TOKEN }}
          access_secret: ${{ secrets.LP_ACCESS_SECRET }}
      - name: MM Failure
        if: ${{ failure() }}
        run: |
          curl -i -X POST -H 'Content-Type: application/json' -d '{"username" : "github-builds", "text" : "<!channel> :warning: Launchpad build failed [${{github.event_name}}] ${{github.workflow}} [See logs](https://github.com/canonical/edgex-sync/actions/runs/${{github.run_id}}) "}' ${{secrets.MATTERMOST}}
```

This stage uses the [edgex-launchpad-build-action](https://github.com/canonical/edgex-launchpad-build-action) Github Action.

## Creating a new workflow


Each snap has its workflow file in the [.github/workflows](https://github.com/canonical/edgex-sync/tree/main/.github/workflows) directory.  They are set to run once a day to create the daily latest/edge release.

To create a new workflow for your snap, do the following:

1. Create a fork of the https://github.com/canonical/edgex-sync repository in your personal github account. Create a new feature branch and use that for the changes you make

2. Create your workflow file by copying one of the existing workflow files.

3. Edit your new workflow file. Assuming you are using wf-edgexfoundry.yml as the basis, you need to make the following changes:

- Change the name of the workflow, in line 1. This is the name used in logs and reports, including the MatterMost messages we get when errors occur.

    ``` 
    name: EdgeXFoundry-Snap
    ```

- In `build-snap`: Change the name of the repository from edgex-go to the name of the new repository you created
      
    ```
    repository: edgexfoundry/edgex-go
    ```

- In `build-launchpad`: Change the name of the snap from edgexfoundry to the name of your snap:
		
    ```
    edgex_snap: "edgexfoundry"
    ```
